use anyhow::{bail, Result};
use std::env;
use util::read_one_per_line;

fn solve_part_one(input: &Vec<u32>) -> Result<usize> {
    Ok(input.windows(2).filter(|w| w[0] < w[2 - 1]).count())
}

fn solve_part_two(input: &Vec<u32>) -> Result<usize> {
    // definitely borrowed from https://www.youtube.com/watch?v=G3JDYAiX5PU
    Ok(input.windows(4).filter(|w| w[0] < w[4 - 1]).count())
}

fn main() -> Result<()> {
    let input;
    if let Some(file) = env::args().nth(1) {
        println!("=> Got filename: {}", &file);
        input = read_one_per_line::<u32>(&file)?;
    } else {
        bail!("Hey!, We need a filename.")
    }

    println!("Part 1: {}", solve_part_one(&input)?);
    println!("Part 2: {}", solve_part_two(&input)?);

    Ok(())
}
