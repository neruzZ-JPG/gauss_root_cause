python .\read_smooth_detection.py > run.out
python .\calculate_correlation.py >> run.out
python .\construct_graph.py >> run.out
python .\rank.py >> run.out
python .\evaluation.py >> run.out