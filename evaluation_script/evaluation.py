#!/usr/bin/env python
import sys
import os.path
import pandas as pd
import numpy as np
from scipy import stats

def check_file(path, correct_number_of_columns):
    df = pd.read_csv(path)
    if (len(df.columns) != correct_number_of_columns):
        sys.exit('Column format problem.')
    if (list(df.columns)[0].lower() != 'pairid'):
        sys.exit('Your submission has no header. Please provide a file with header as: PairID,Pred_Score')
    

def evaluate(pred, gold):
    
    check_file(pred, 2)
    check_file(gold, 2)

    print('Files format checked successfully')

    pred_lines = pd.read_csv(pred, header=0, names=['pairid', 'pred_score'])
    gold_lines = pd.read_csv(gold, header=0, names=['pairid', 'score'])

    if(len(pred_lines)==len(gold_lines)):
        
        # align tweets ids with gold scores and predictions
        try:
            data_dic = gold_lines.set_index('pairid').to_dict(orient='dict')['score']
            data_dic = {k: [v] for k, v in data_dic.items()}
        except:
            sys.exit('Format problem.')
        
        for key, value in pred_lines.set_index('pairid').to_dict(orient='dict')['pred_score'].items():
            if key and str(value):
                if key in data_dic:
                    try:
                        data_dic[key].append(value)
                    except ValueError:
                        sys.exit('Cannot append score.')
                else:
                    sys.exit('Invalid pair id. Make sure the submission is correct.')
            else:
                print(key, value)
                sys.exit('Format problem.')
            
        
        # lists storing gold and prediction scores
        gold_scores=[]
        pred_scores=[]
        
        # check if all ids have gold and prediction scores    
        for id in data_dic:
            if(len(data_dic[id])==2):
                gold_scores.append(data_dic[id][0])
                pred_scores.append(data_dic[id][1])   
            else:
                sys.exit('Repeated id in test data.')

        # compute spearman correlation
        #df = pd.DataFrame(zip(gold_scores, pred_scores), columns=['gold', 'pred'])
        return stats.spearmanr(np.array(gold_scores), np.array(pred_scores))[0]
       
    else:
        sys.exit('Predictions and gold data have different number of lines.')
        

def main(argv):

    # get input and output directories from command line
    [input_dir, output_dir] = argv

    # get gold standard file path
    ref_dir = os.path.join(input_dir, 'ref')
    gold_standard = os.path.join(ref_dir, os.listdir(ref_dir)[0])

    # get language from gold standard file name
    lang = gold_standard.split('/')[-1].split('_')[0]
    
    # get submission file path
    submission_path = os.path.join(input_dir, 'res', 'pred_' + lang + '.csv')

    # check if submission file exists
    if not os.path.exists(submission_path):
        sys.exit('Could not find submission file {0}, please check the submission file name.'.format(submission_path))
    
    # evaluate submission
    eval_scores = evaluate(submission_path, gold_standard)

    # write scores to output file
    with open(os.path.join(output_dir, 'scores.txt'),"w") as output_file:
        output_file.write("spearman_cor:{0}\n".format(eval_scores))

    with open(os.path.join(output_dir, 'detailed_results.html'), 'w') as html_file:
        html_file.write("<html><head><title>Results</title></head><body><p>Your Spearman Correlation: {0}</p></body></html>".format(eval_scores))
    
if __name__ == "__main__":
    main(sys.argv[1:])