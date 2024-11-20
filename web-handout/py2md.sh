#!/bin/bash

# Check if input and output directories are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <input_directory> <output_directory>"
  exit 1
fi

INPUT_DIR=$1
OUTPUT_DIR=$2

# Check if input directory exists
if [ ! -d "$INPUT_DIR" ]; then
  echo "Error: Input directory '$INPUT_DIR' does not exist."
  exit 1
fi

# Create output directory if it does not exist
if [ ! -d "$OUTPUT_DIR" ]; then
  mkdir -p "$OUTPUT_DIR"
  echo "Created output directory '$OUTPUT_DIR'."
fi

# Clear the output directory
rm -f "$OUTPUT_DIR"/*

# Traverse through each file in the input directory
for file in "$INPUT_DIR"/*; do
  # Check if it's a file
  if [ -f "$file" ]; then
    # Extract the file name without the directory
    base_name=$(basename "$file")
    
    # Ensure the new file name is constructed correctly
    new_file="$OUTPUT_DIR/$base_name.md"
  
    # Paste the code content
    echo "---" > "$new_file"
    echo "layout: code" >> "$new_file"
    echo "title: $base_name" >> "$new_file"
    echo "---" >> "$new_file"
    echo "" >> "$new_file"
    echo "\`\`\`python" >> "$new_file"
    cat "$file" >> "$new_file"
    echo "\`\`\`" >> "$new_file"
    
    echo "Processed $file -> $new_file"
  fi
done
