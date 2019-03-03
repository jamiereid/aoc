#[macro_use]
extern crate failure;

use std::env;
use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use failure::ResultExt;

fn read_in_file(file: &str) -> Result<String, failure::Error> {
    let of = File::open(file).context(format!("Failed to open file {}", file))?;
    let mut buf_reader = BufReader::new(of);
    let mut contents = String::new();
    buf_reader.read_to_string(&mut contents).context("Had trouble reading file contents to String")?;

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

    println!("{}", input);

    Ok(())
}
