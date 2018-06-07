#import sys
from feature_format import featureFormat

def min_max_ex_stock_opt(data_dict):
    """ Prints min and max exercised stock options
        data_dict = The data dictionary containing exercised stock options
    """
 
    # max_eso = data_dict[ max( data_dict, key=lambda x: None if
    #           data_dict[x]['exercised_stock_options']=='NaN' else
    #           float(data_dict[x]['exercised_stock_options']) ) ]['exercised_stock_options'] 
    # min_eso = data_dict[ min( data_dict, key=lambda x: sys.float_info.max if
    #           data_dict[x]['exercised_stock_options']=='NaN' else
    #           float(data_dict[x]['exercised_stock_options']) ) ]['exercised_stock_options']

    max_eso = max( featureFormat(data_dict, ["exercised_stock_options"]) )
    min_eso = min( featureFormat(data_dict, ["exercised_stock_options"]) )

    print("Max: {} | Min: {}".format(max_eso, min_eso) )

def min_max_feature(data_dict, feature):
    """ Prints min and max of given features from the data dictionary 
        data_dict =     
            The data dictionary containing features
        feature = 
            The feature for which min and max is to be determined
    """
    max_val = max( featureFormat(data_dict, [feature]) )
    min_val = min( featureFormat(data_dict, [feature]) )

    print("Max {}: {} | Min {}: {}".format(feature, max_val, feature, min_val) )                  