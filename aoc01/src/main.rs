#[macro_use]
extern crate failure;

use failure::ResultExt;
use std::env;
use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;

fn read_in_file(file: &str) -> Result<String, failure::Error> {
    let of = File::open(file).context(format!("Failed to open file {}", file))?;
    let mut buf_reader = BufReader::new(of);
    let mut contents = String::new();
    buf_reader
        .read_to_string(&mut contents)
        .context("Had trouble reading file contents to String")?;

    Ok(contents)
}

fn main() -> Result<(), failure::Error> {
    let input;
    if let Some(file) = env::args().nth(1) {
        println!("=> Got filename: {}", file);
        input = read_in_file(&file)?;
    } else {
        bail!("Hey!, We need a filename.")
    }

    let freq: isize = input.lines().fold(0, |acc, line| {
        let c: isize = line.parse().unwrap(); // @Note: we're guaranteed good input, so we're just using unwrap. @Study: a better way!
        acc + c
    });
    println!("{}", freq);
    Ok(())
}
