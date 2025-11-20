#!/bin/bash
# IOzone benchmark script for Docker environment
# This script runs various I/O benchmarks using IOzone

echo "Starting IOzone benchmark..."

# Create a test directory
TEST_DIR="/root/iozone_test"
mkdir -p $TEST_DIR

# Run IOzone with various file sizes and record types
# -a: Full automatic mode
# -R: Generate Excel compatible output
# -b: Generate binary output file
# -i: Test types (0=write/rewrite, 1=read/reread, 2=random-read/write)

iozone -a -R -i 0 -i 1 -i 2 -s 512M -f $TEST_DIR/testfile > /root/iozone_results.txt

echo "IOzone benchmark complete. Results saved to /root/iozone_results.txt"

# Clean up
rm -rf $TEST_DIR
