python .\read_smooth_detection.py 2> run.out
python .\calculate_correlation.py 2>> run.out
python .\construct_graph.py 2>> run.out
python .\rank.py 2>> run.out
python .\evaluation.py 2>> run.out