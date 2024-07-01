#!/usr/bin/env python
import argparse
import nbformat
from nbformat import NotebookNode

def replace_solution_cells(notebook_path: str, output_path: str) -> None:
    # Load the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
    
    # Create a new notebook object to hold modified cells
    new_nb = NotebookNode(nbformat=nb.nbformat, nbformat_minor=nb.nbformat_minor, metadata=nb.metadata, cells=[])


    # Iterate through the cells
    for cell in nb.cells:
        # Check if the cell has tags and if 'solution' is one of the tags
        if 'metadata' in cell and 'tags' in cell.metadata and 'solution' in cell.metadata.tags:
            # Create a new empty cell based on the cell type
            if cell.cell_type == 'code':
                # Create a code cell with placeholder text
                new_cell = nbformat.v4.new_code_cell(source="# code here")
            elif cell.cell_type == 'markdown':
                # Create a markdown cell with placeholder text
                new_cell = nbformat.v4.new_markdown_cell(source="*Answer here*")
            new_nb.cells.append(new_cell)  # Add new cell to the new notebook
        else:
            new_nb.cells.append(cell)  # Add untagged cell to the new notebook

    # Write the new notebook to the output path
    with open(output_path, 'w', encoding='utf-8') as f:
        nbformat.write(new_nb, f)

    print(f"Notebook saved with placeholders for 'solution' tagged cells to {output_path}")

def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Remove cells with 'solution' tag from a Jupyter Notebook.")
    
    # Add the arguments
    parser.add_argument("input_notebook", help="Path to the input Jupyter Notebook")
    parser.add_argument("-o", "--output_notebook", help="Path to the output Jupyter Notebook", default=None)

    # Parse the arguments
    args = parser.parse_args()

    input_notebook = args.input_notebook
    # Set the output notebook name based on the input name if not provided
    output_notebook = args.output_notebook if args.output_notebook else f"{input_notebook.rsplit('.', 1)[0]}_processed.ipynb"

    # Call the function with the command-line arguments
    replace_solution_cells(input_notebook, output_notebook)

if __name__ == "__main__":
    main()
