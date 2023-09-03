use std::{collections::VecDeque, fs::read_to_string, ops::Add};

pub fn main() {
    let mut monkeys = Vec::with_capacity(4);
    let starting_items = parse_file("inputs/day11.in");

    monkeys.push(Monkey::new(VecDeque::new(), '+', 7, 1, 2));

    println!("monkey 0, stress_operator: {}", monkeys[0].stress_operator);
}

#[derive(Debug)]
struct Monkey {
    items: VecDeque<i32>,
    stress_operator: char,
    test_divisible_by: i32,
    throw_to_if_true: u8,
    throw_to_if_false: u8,
}

impl Monkey {
    fn new(
        items_list: VecDeque<i32>,
        op: char,
        test: i32,
        if_true_id: u8,
        if_false_id: u8,
    ) -> Monkey {
        Monkey {
            items: items_list,
            stress_operator: op,
            test_divisible_by: test,
            throw_to_if_true: if_true_id,
            throw_to_if_false: if_false_id,
        }
    }

    fn operation(stress_operator: char, a: i32, b: i32) -> i32 {
        if stress_operator == '+' {
            a.add(b)
        } else if stress_operator == '*' {
            a * b
        } else {
            panic!(
                "ERROR: stress_operator is {}, but should be in '+', '*'",
                stress_operator.to_string()
            );
        }
    }
}

fn parse_file(filename: &str) -> VecDeque<String> {
    read_to_string(filename)
        .unwrap() // panic on possible file-reading errors
        .lines() // split the string into an iterator of string slices
        .map(String::from) // make each slice into a string
        .collect() // gather them together into a vector
}
