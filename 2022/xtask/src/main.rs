use anyhow::Result;
use clap::{Parser, Subcommand};

#[derive(Debug, Parser)]
#[clap(max_term_width = 120, about = "helper tasks for Advent Of Code")]
struct Xtask {
    #[command(subcommand)]
    command: Commands,
}

#[derive(Debug, Subcommand)]
enum Commands {
    /// Create a new directory ready for the day's puzzles
    #[command(arg_required_else_help = false)]
    Newday {
        /// the day of the month to create (eg 1 to 31)
        day: Option<u8>,
    },
}

fn newday(day: Option<u8>) -> Result<()> {
    use cargo_metadata::MetadataCommand;
    let metadata = MetadataCommand::new()
        .manifest_path("./Cargo.toml")
        .exec()
        .unwrap();

    let root = std::path::PathBuf::from(metadata.workspace_root);
    dbg!(root);

    // if an was arg provided use it, otherwise try to find the last created date
    let dir_name_to_create;
    if let Some(d) = day {
        dbg!(d);
        dir_name_to_create = format!("day{:02}", d);
    } else {
        // try to find the last created date
        dir_name_to_create = "dayincomplete".to_string();
    }

    dbg!(dir_name_to_create);

    Ok(())
}

fn main() -> Result<()> {
    let xtask = Xtask::parse();

    match xtask.command {
        Commands::Newday { day } => newday(day)?,
    }

    Ok(())
}
