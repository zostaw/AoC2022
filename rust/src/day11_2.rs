use std::{
    collections::{HashMap, VecDeque},
    fs::read_to_string,
    ops::Add,
};

//common multiple for the divisible checks and number reduction
const COMMON_MULTIPLE: u64 = 9699690;

pub fn main() {
    let mut monkeys = parse_file_monkeys("inputs/day11.in");

    print_monkeys(&monkeys);
    // let common_multiple: u64 = monkeys
    //     .iter()
    //     .map(|(_, monkey)| monkey.test_divisible_by)
    //     .product();
    // println!("common multiple: {}", common_multiple);

    //let no_rounds = 20;
    let no_rounds = 10000;
    for counter in 0..no_rounds {
        println!("Round {}", counter);
        round(&mut monkeys);
        print_monkeys(&monkeys);
    }

    monkey_business(&monkeys);
}

fn round(monkeys: &mut HashMap<usize, Monkey>) {
    let monkeys_len = monkeys.len();

    for id in 0..monkeys_len {
        let mut monkeys_throw_list: VecDeque<(usize, u64)>;

        let Some(mut monkey) = monkeys.remove(&id) else {
            panic!("No monkey found in monkeys.")
        };
        // decide upon items
        monkeys_throw_list = monkey.inspect_items();

        while let Some((id, val)) = monkeys_throw_list.pop_front() {
            let throw_monkey = monkeys.get_mut(&id);
            throw_monkey.unwrap().items.push_back(val);
        }

        monkeys.insert(id, monkey);
    }
}

fn print_monkeys(monkeys: &HashMap<usize, Monkey>) {
    let monkeys_len = &monkeys.len();
    for monkey_id in 0..*monkeys_len {
        let monkey = &monkeys[&monkey_id];

        println!("monkey {}: {:?}", monkey_id, &monkey);
    }
}

fn monkey_business(monkeys: &HashMap<usize, Monkey>) {
    let mut monkey_business: [u64; 2] = [0; 2];

    let monkeys_len = &monkeys.len();
    for monkey_id in 0..*monkeys_len {
        let monkey_val = monkeys.get(&monkey_id).unwrap().business;
        if monkey_val > monkey_business[0] || monkey_val > monkey_business[1] {
            if monkey_business[0] > monkey_business[1] {
                monkey_business[1] = monkey_val;
            } else {
                monkey_business[0] = monkey_val;
            }
        }
    }
    let quotient = monkey_business[0] * monkey_business[1];
    println!("Most active quotiend: {:?}", quotient);
}

#[derive(Debug)]
#[allow(dead_code)]
struct Monkey {
    items: VecDeque<u64>,
    stress_operator: (char, String),
    test_divisible_by: u64,
    throw_to_if_true: usize,
    throw_to_if_false: usize,
    business: u64,
}

impl Monkey {
    fn new(
        items_list: VecDeque<u64>,
        op: (char, String),
        test: u64,
        if_true_id: usize,
        if_false_id: usize,
        business: u64,
    ) -> Monkey {
        Monkey {
            items: items_list,
            stress_operator: op,
            test_divisible_by: test,
            throw_to_if_true: if_true_id,
            throw_to_if_false: if_false_id,
            business,
        }
    }

    fn operation(&self, mut item: u64) -> u64 {
        // performs operation depending on stress_operator
        // if stress_operator.1 has value <u64>, it will return: item = item +/* stress_operator.1
        // otherwise (if stress_operator.1 is string 'old') it will return: item = item +/* item

        let op = self.stress_operator.0;
        let op_val: u64;

        // define action
        if &self.stress_operator.1 == &"old" {
            //return item;
            op_val = item.clone();
        } else {
            op_val = match self.stress_operator.1.parse::<u64>() {
                Ok(val) => val,
                Err(_) => {
                    panic!("stress_operator value should be either 'old' or <u64>, but is neither.")
                }
            };
        }

        // perform operation
        if op == '+' {
            item = item.add(op_val);
        } else if op == '*' {
            item = item * op_val;
        } else {
            panic!("ERROR: op is {}, but should be in '+', '*'", op);
        }

        //let temp_item = item as f64 / 3_f64;
        //item = temp_item.floor() as u64;

        return item;
    }

    fn inspect(&mut self, mut item: u64) -> (usize, u64) {
        item = self.operation(item);
        let throw_monkey_id: usize;
        self.business += 1;

        item = item % COMMON_MULTIPLE;

        if item % self.test_divisible_by == 0 {
            throw_monkey_id = self.throw_to_if_true;
        } else {
            throw_monkey_id = self.throw_to_if_false;
        }

        return (throw_monkey_id, item);
    }

    fn inspect_items(&mut self) -> VecDeque<(usize, u64)> {
        let mut monkeys_throw_list: VecDeque<(usize, u64)> = VecDeque::new();

        while let Some(item) = self.items.pop_front() {
            monkeys_throw_list.push_back(self.inspect(item));
        }

        return monkeys_throw_list;
    }
}

fn parse_file_monkeys(filename: &str) -> HashMap<usize, Monkey> {
    // expected file format:
    // "Monkey [0]",
    // "Starting items: [<list>]",
    // "  Operation: new = old [<operator>] ['old'/<u64>]",
    // "  Test: divisible by [<u64>]",
    // "    If true: throw to monkey [<usize>]",
    // "    If false: throw to monkey [<usize>]",
    // "",
    // "Monkey [1]",
    // "Starting items: [<list>]",
    // "  Operation: new = old [<operator>] ['old'/<u64>]",
    // "  Test: divisible by [<u64>]",
    // "    If true: throw to monkey [<usize>]",
    // "    If false: throw to monkey [<usize>]",
    // "",
    // ...

    let mut monkeys: HashMap<usize, Monkey> = HashMap::new();
    let file_lines: Vec<String> = read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from)
        .collect(); // make each slice into a string
    let mut file_lines_iter = file_lines.iter();
    let mut id = 0;

    while let Some(line) = file_lines_iter.next() {
        let f_lines_iter_ref = &mut file_lines_iter;

        // search until Monkey found
        if !line.contains("Monkey ") {
            continue;
        }

        //println!("[DEBUG] New {}", line);
        let items_list = parse_items_list(&f_lines_iter_ref.next().unwrap());
        //println!("[DEBUG] Items list: {:?}", items_list);
        let op = parse_op(&f_lines_iter_ref.next().unwrap());
        //println!("[DEBUG] Operation: {:?}", op);
        let test = parse_test(&f_lines_iter_ref.next().unwrap());
        //println!("[DEBUG] Test: {:?}", test);
        let if_true_id = parse_if_true_id(&f_lines_iter_ref.next().unwrap());
        //println!("[DEBUG] If true: {:?}", if_true_id);
        let if_false_id = parse_if_false_id(&f_lines_iter_ref.next().unwrap());
        //println!("[DEBUG] If false: {:?}", if_false_id);

        monkeys.entry(id).or_insert(Monkey::new(
            items_list,
            op,
            test,
            if_true_id,
            if_false_id,
            0,
        ));
        id += 1;
    }

    return monkeys;

    fn parse_items_list(line: &str) -> VecDeque<u64> {
        if !line.contains(&"  Starting items: ") {
            panic!(
                "Error in parsing, expected '  Starting items: ', but not found in '{}'. 
                Is file format correct? Check if items are in correct order.",
                line
            );
        }

        //println!("[DEBUG] New starting items record - {:?}", line);
        let result_vecdeq: Vec<u64> = line
            .replace("  Starting items: ", "")
            .split(", ")
            .map(|val| {
                val.parse::<u64>()
                    .expect("Could not parse items_list as u64.")
            })
            .collect::<Vec<u64>>();
        return result_vecdeq.into();
    }

    fn parse_op(line: &str) -> (char, String) {
        if !line.contains(&"  Operation: new = old ") {
            panic!(
                "Error in parsing, expected '  Operation: new = old ', but not found in '{}'.
                Is file format correct? Check if items are in correct order.",
                line
            );
        }

        //println!("[DEBUG] New Operation record - {:?}", line);
        let result_op: Vec<char> = line
            .replace("  Operation: new = old ", "")
            .chars()
            .collect();

        let op: char = result_op[0];
        let val: String = result_op[2..]
            .iter()
            .map(|v| String::from(v.to_owned()))
            .collect();

        // val must be either 'old' or <u64>
        if &val == &"old" {
            return (op, val);
        }

        match &val.parse::<u64>() {
            Err(e) => panic!("Operand should be either 'old' or <u64>, but found ({})", e),
            Ok(_) => (),
        };

        return (op, val);
    }

    fn parse_test(line: &str) -> u64 {
        if !line.contains(&"  Test: divisible by ") {
            panic!(
                "Error in parsing, expected '  Test: divisible by ', but not found in '{}'. 
                Is file format correct? Check if items are in correct order.",
                line
            );
        }

        line.replace("  Test: divisible by ", "")
            .parse::<u64>()
            .expect("Test: divisible by <u64> expected, but received something else.")
    }

    fn parse_if_true_id(line: &str) -> usize {
        if !line.contains(&"    If true: throw to monkey ") {
            panic!(
                "Error in parsing, expected '    If true: throw to monkey ', but not found in '{}'. 
                Is file format correct? Check if items are in correct order.",
                line
            );
        }

        line.replace("    If true: throw to monkey ", "")
            .parse::<usize>()
            .expect("    If true: throw to monkey <usize> expected, but received something else.")
    }

    fn parse_if_false_id(line: &str) -> usize {
        if !line.contains(&"    If false: throw to monkey ") {
            panic!(
                "Error in parsing, expected '    If false: throw to monkey ', but not found in '{}'. 
                Is file format correct? Check if items are in correct order.",
                line
            );
        }

        line.replace("    If false: throw to monkey ", "")
            .parse::<usize>()
            .expect("    If false: throw to monkey <usize> expected, but received something else.")
    }
}
