# Study Compass

Study Compass is a personal CLI tool for recording study activities, tracking progress, and generating reflections.

It is designed for my daily learning process, including:
- algorithm practice
- course learning
- project progress
- weekly review

## Overview

I built this project to make my study records more structured and easier to review.

In daily learning, it is easy for useful information to become scattered across notes, temporary plans, or unfinished thoughts. This project is my attempt to turn those fragmented learning activities into clear, searchable, and reusable records.

Rather than building a project only for demonstration, I want this to be a tool I can actually use in real life.

## Features

The current version supports:
- adding a study record
- viewing all saved records
- filtering records by date, category, title, tag, status, difficulty, blocker, or note
- managing records through view, edit, and delete actions
- storing records locally in JSON format
- organizing records with structured fields

Each record may include:
- id
- date
- category
- title
- tags
- status
- difficulty
- blockers
- note

## Why I Made This Project

This project started from a simple need:

I often work on multiple kinds of tasks at the same time, such as solving algorithm problems, studying university courses, and building small projects. Without a structured way to record them, it becomes difficult to review progress, identify repeated problems, or build long-term learning habits.

So I created this tool to help myself:
- record what I am learning
- track how I am progressing
- notice where I get stuck
- reflect on my study process more clearly

## Project Structure

```text
.
├─ main.py
├─ models.py
├─ record_constants.py
├─ record_query.py
├─ record_ui.py
├─ record_workflow.py
├─ storage.py
├─ requirements.txt
├─ data/
│  └─ record.json
└─ README.md
```

## Usage

Run the program with:
python main.py

Then choose from the available options in the CLI interface to:
- add a new record
- view existing records
- filter records
- manage records
- exit
When creating a record, the program will guide you through:
- basic information
- topic and method
- completion quality
- reflection and notes

## Storage

Records are stored locally in `data/record.json` using JSON format.

The program automatically:
- loads existing records
- assigns unique ids to new records
- normalizes date values
- writes updates back to local storage

## Example Record

Here is an example of a study record:

```json
{
  "id": 3,
  "date": [2026, 3, 15],
  "category": "problem",
  "title": "P1216 Number Triangles",
  "tags": ["dynamic-programming", "linear-dp"],
  "status": "solved",
  "difficulty": 2,
  "blockers": ["State transition was not clear at first."],
  "note": "A classic introductory DP problem."
}
```

## Design Idea

The core idea of this project is simple:
- keep study records lightweight
- preserve useful context
- make later review easier
- gradually build a clearer picture of long-term learning

Instead of writing long and irregular notes every time, I prefer a structured format that is quick to record and easy to analyze later.

## Development Goal
I hope this project can gradually grow from a simple record keeper into a practical personal learning companion.

At the same time, this repository is also a record of my growth in:
- designing tools for real use
- organizing personal data
- thinking about how software can support learning

## Future Plans

Possible future improvements include:
- sorting records by date or difficulty
- exporting records to other formats
- generating weekly or monthly summaries
- improving the CLI interaction experience
- adding basic statistics and visual summaries

## Note

This is a personal learning project and is still under active development.

The structure, implementation, and features may continue to change as I improve both the tool itself and my understanding of my own study workflow.
