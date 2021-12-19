use anyhow::{Context, Result};

use std::fs::File;
use std::io::prelude::*;
use std::io::BufReader;
use std::str::FromStr;

fn read_in_file(file: &str) -> Result<String> {
    let file = File::open(file).context(format!("Failed to open file {}", file))?;
    let mut buf_reader = BufReader::new(file);
    let mut contents = String::new();

    buf_reader
        .read_to_string(&mut contents)
        .context("Had trouble loading file contents in read_in_file")?;

    Ok(contents)
}

pub fn read_one_per_line<T>(path: &str) -> Result<Vec<T>>
where
    T: FromStr,
{
    Ok(read_in_file(path)?
        .split("\n")
        .filter_map(|l| l.parse::<T>().ok())
        .collect())
}
