import sys
import os

def calculate_gc_content(sequence):
    """Calculate the GC content of a DNA sequence as a percentage."""
    sequence = sequence.upper()  # Convert to uppercase to handle both cases
    total_bases = len(sequence)
    if total_bases == 0:
        print("Warning: Empty sequence")
        return 0.0
    gc_count = sequence.count('G') + sequence.count('C')
    return (gc_count / total_bases) * 100

def validate_sequence(sequence):
    """Validate that the sequence contains only valid DNA characters."""
    valid_chars = set('ATCG')
    sequence = sequence.upper()
    invalid_chars = set(sequence) - valid_chars
    if invalid_chars:
        print(f"Warning: Found invalid characters in sequence: {invalid_chars}")
        return False
    return True

def read_fasta_file(filename):
    """Read a FASTA file and return the DNA sequence, ignoring header lines."""
    sequence = ""
    try:
        # Print absolute path for debugging
        abs_path = os.path.abspath(filename)        
        if not os.path.exists(abs_path):
            print(f"Error: File '{abs_path}' does not exist.")
            sys.exit(1)
            
        with open(abs_path, 'r') as file:
            print("File opened successfully")
            print(file)
            line_count = 0
            for line in file:
                line_count += 1
                line = line.strip()
                if not line:  # Skip empty lines
                    continue
                if line.startswith('>'):
                    print(f"Found header line: {line}")
                    continue
                sequence += line
                
            print(f"Read {line_count} lines")
            if not sequence:
                print("Warning: No sequence data found in file")
                
        return sequence
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {str(e)}")
        sys.exit(1)

def main():
    # Check if filename is provided as command line argument
    if len(sys.argv) != 2:
        print("Usage: python GC_content_calculator.py <fasta_file>")
        print("Current working directory:", os.getcwd())
        sys.exit(1)
    
    # Get filename from command line argument
    filename = sys.argv[1]
    
    # Read the sequence from the file
    sequence = read_fasta_file(filename)
    
    print(f"Read sequence length: {len(sequence)}")
    if sequence:
        print(f"First 50 characters: {sequence[:50]}...")
    
    # Validate sequence
    if not validate_sequence(sequence):
        print("Warning: Sequence contains invalid characters")
    
    # Calculate and print GC content
    gc_content = calculate_gc_content(sequence)
    print(f"GC content: {gc_content:.2f}%")

if __name__ == "__main__":
    main()
