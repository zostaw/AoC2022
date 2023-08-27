use std::fs::read_to_string;
use std::collections::VecDeque;

//static NUMBER_OF_CYCLES: usize = 180;
static NUMBER_OF_CYCLES: usize = 220;

fn read_instruction (state: &mut i32, queue: &mut VecDeque<i32>) {
    if let Some(value) = queue.pop_front() {
        println!("Processing instruction: {}", &value);
        *state += value;
    }
}

fn clock_circuit(state: &mut i32, mut queue: VecDeque<i32>, number_of_cycles: usize) -> i32 {
    let mut signal_strength_sum: i32 = 0;

    // count from 1
    let mut cycle = 1;
    while cycle <= number_of_cycles {
        // read instruction
        println!("cycle is: {} and state is: {}", &cycle, &state);
         
        // at 20 and every 40 afterwards
        if cycle == 20 || cycle >= 60 && (cycle - 20) % 40 == 0 {
            signal_strength_sum += *state * (cycle as i32);
        }

        read_instruction(&mut *state, &mut queue);

        cycle += 1;
    }

    return signal_strength_sum;

}


fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()  // panic on possible file-reading errors
        .lines()  // split the string into an iterator of string slices
        .map(String::from)  // make each slice into a string
        .collect()  // gather them together into a vector
}
fn preprocess_stack(str_stack: Vec<String>) -> VecDeque<i32> {
    let mut queue: VecDeque<i32> = VecDeque::new();

    for line in str_stack{
        if line == "noop"{
            queue.push_back(0);
        } else {
            // split line and unpack int value
            let mut split = line.split(" ");
            let my_tuple = (split.next().unwrap(), split.next().unwrap());
            let my_int = my_tuple.1.parse::<i32>().unwrap();
            
            // 2 cycles: 0 -> value
            queue.push_back(0);
            queue.push_back(my_int);
        }
    }

    return queue;
}

fn main() {
    let mut state: i32 = 1;
    let sum: i32;
    
    // Load file and format into clock_circuit format
    let str_stack = read_lines("./inputs/day10.in");
    let queue: VecDeque<i32> = preprocess_stack(str_stack);

//    for foo in 0..NUMBER_OF_CYCLES {
//        println!("queue[{}]: {}", &foo, &queue[foo]);
//    }

    // cycle through stack
    sum = clock_circuit(&mut state, queue, NUMBER_OF_CYCLES);

    println!("State at {} is {} and the sum is {}", NUMBER_OF_CYCLES, state, sum);
}
