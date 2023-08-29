use std::fs::read_to_string;
use std::collections::VecDeque;

//static NUMBER_OF_CYCLES: usize = 180;
const NUMBER_OF_CYCLES: usize = 240;

fn read_instruction (state: &mut i32, queue: &mut VecDeque<i32>) {
    if let Some(value) = queue.pop_front() {
        println!("Processing instruction: {}", &value);
        *state += value;
    }
}

fn draw_pixel(cycle: usize, sprite_position: i32) -> char {
    // sprite is 3 pixels wide
    if (sprite_position - cycle as i32).abs() < 2 {
        return '#';
    };
    return '.';

}

fn clock_circuit(mut sprite_position: i32, mut queue: VecDeque<i32>) -> [char; NUMBER_OF_CYCLES] {
    let mut screen: [char; NUMBER_OF_CYCLES] = ['.'; NUMBER_OF_CYCLES];

    // count from 0
    let mut cycle = 0;
    while cycle < NUMBER_OF_CYCLES {
        // read instruction
        println!("cycle is: {} and state is: {}", &cycle, &sprite_position);

        screen[cycle] = draw_pixel(cycle, sprite_position);

        read_instruction(&mut sprite_position, &mut queue);

        cycle += 1;
        if cycle%40 == 0 {
            sprite_position += 40;
        }
    }

    return screen;

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
    let state: i32 = 1;
    
    // Load file and format into clock_circuit format
    let str_stack = read_lines("./inputs/day10.in");
    let queue: VecDeque<i32> = preprocess_stack(str_stack);

    let screen = clock_circuit(state, queue);

    println!("Output:\n{:?}\n{:?}\n{:?}\n{:?}\n{:?}\n{:?}", 
             &screen[0..40],
             &screen[40..80],
             &screen[80..120],
             &screen[120..160],
             &screen[160..200],
             &screen[200..240]);
}
