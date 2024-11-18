# Quicksort Implementation and Analysis

This project implements and analyzes two variations of the Quicksort algorithm: deterministic and randomized. The implementation includes performance comparisons across different input distributions and sizes.

## Implementation Files

- `quicksort.py`: Contains the deterministic Quicksort implementation
- `randomized_quicksort.py`: Contains the randomized Quicksort implementation
- `empiricalAnalysis.py`: Contains the testing framework and performance analysis

## Requirements

- Python 3.x
- NumPy library (`pip install numpy`)

## Installation

1. Clone this repository or download the source files
2. Install the required dependencies:
```bash
pip install numpy
```

## Usage

To run the empirical analysis:

```bash
python empiricalAnalysis.py
```

The program will output a table comparing the performance of both implementations across different input sizes and distributions.

## Implementation Details

### Deterministic Quicksort
- Uses the last element as the pivot
- Implements tail-call optimization to limit recursion depth
- Located in `quicksort.py`

### Randomized Quicksort
- Selects a random pivot for each partition
- Implements tail-call optimization to limit recursion depth
- Located in `randomized_quicksort.py`

## Key Findings

1. **Performance Characteristics**
   - Both implementations perform efficiently on small input sizes (<1ms)
   - Randomized Quicksort shows consistent O(n log n) scaling
   - Deterministic version shows more variability with sorted inputs

2. **Distribution Effects**
   - Randomized version maintains consistent performance across all input distributions
   - Deterministic version shows slight variation with sorted and reverse-sorted arrays

3. **Stability and Safety**
   - Randomized Quicksort provides more reliable performance guarantees
   - Lower risk of hitting worst-case O(n²) performance in randomized version
   - More even partitioning observed in randomized implementation

## Performance Results

The analysis tests both implementations against:
- Input sizes: 1000, 5000, and 10000 elements
- Distribution types: Random, Sorted, and Reverse-Sorted arrays


