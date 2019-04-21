from data_getter import *
from date_processing import *

if __name__ == '__main__':
    data = get_by_time_delta('2015-1-1', 10, 'pm25')
    # std_out = get_std_and_var(data,'pm25')
    # d_list = morkov_get_status_list(std_out)
    # state_list = morkov_get_state_list(data,'pm25',d_list)
    # matrix = morkov_get_transfer_matrix(state_list)
    # w_list = morkov_get_w_list(data,'pm25',std_out)
    # morkov_final(w_list,state_list,matrix,d_list)
    real = data.iloc[3]
    print(real)
