import math
import pandas as pd
import numpy as np
import time
# function for flipping cake pieces
def flip(start, theta, cake, i, tol = 0.01, debug = True):
    
    end = (start + theta) % 360
    if end < start:
        cake['to_be_flipped'] = ((cake['degrees'] >= start) & (cake['degrees'] <= 360) | (cake['degrees'] <= end) )
    else:
        cake['to_be_flipped'] = (cake['degrees'] >= start) & (cake['degrees'] <= end)
    cake['status'] = (cake['to_be_flipped'] * 1 + cake['status']) % 2
    slice_indices = cake.index[cake['to_be_flipped']].tolist()
    print(slice_indices)
    print(cake.loc[slice_indices, 'status'].values)
    reversed_status = cake.loc[slice_indices, 'status'][::-1].values 
    print(reversed_status)
    cake.loc[slice_indices, 'status'] = reversed_status
    
    # debugging
    # print(start)
    # print(end)
    # print(i)
    # print(cake['status'])
    # print(cake['to_be_flipped'])
    if i == 5:
        cake.to_csv('/Users/lukeepp/Downloads/cake{}.csv'.format(i))
        exit()

    cake.drop(columns='to_be_flipped', inplace=True)
    
    start = end
    percent_flipped = sum(cake['status']) / len(cake['status'])
    is_done = percent_flipped < tol
    i += 1

    if debug:
        print('percent flipped after {} steps'.format(i))
        print(percent_flipped)
        #time.sleep(5)
        
    return start, cake, is_done, i




def find_f(A,B,C, num_steps = 360):
    # globals
    DEGREES = 360
    a_deg = DEGREES / A
    b_deg = DEGREES / B
    c_deg = DEGREES / math.sqrt(C)
    # # instantiating other vars
    degrees_vec = np.linspace(0,360,num_steps)
    status_vec = np.repeat(0,num_steps)
    cake_dict = {"degrees": degrees_vec,
                 "status": status_vec}
    cake = pd.DataFrame(cake_dict)
    start = 0
    is_done = False
    i = 0
    while not is_done:
        if i % 3 == 0:
            start, cake, is_done, i = flip(start, a_deg, cake, i)
        elif i % 3 == 1:
            start, cake, is_done, i = flip(start, b_deg, cake, i)
        elif i % 3 == 2:
            start, cake, is_done, i = flip(start, c_deg, cake, i)

    return i


def analytical_find_f(A,B,C):
    DEGREES = 360
    a_deg = DEGREES / A
    b_deg = DEGREES / B
    c_deg = DEGREES / math.sqrt(C)
    cur_sum = 0
    degs_to_flip = 0
    i = 0
    while cur_sum < DEGREES:
        if i % 3 == 0:
            degs_to_flip = a_deg
        elif i % 3 == 1:
            degs_to_flip = b_deg
        elif i % 3 == 2:
            degs_to_flip = c_deg
        cur_sum += degs_to_flip
        i += 1
    print(cur_sum)
    print(i)
    # we have this many degrees unflipped, then we will get that many degrees next to it every i flips
    # we start to get a new pattern after
    remainder = degs_to_flip - (cur_sum - DEGREES)
    guess = DEGREES // remainder
    guess_times_i = guess * i
    print(remainder)
    print(guess)
    print(guess_times_i)
    return 0

# test1 = find_f(6, 6, 6 **2)
# print(test1)

# test2 = find_f(9, 10, 11)
# print(test2)

test2 = analytical_find_f(9, 10, 11)
print(test2)






# def plot_cake(cake):
#     radians = np.deg2rad(cake['degrees'])  # Convert degrees to radians
#     colors = ['white' if status == 0 else '#FFC0CB' for status in cake['status']]  # White for 0, Pink for 1

#     # Plot setup
#     fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
#     ax.set_theta_direction(1)  # Clockwise direction
#     ax.set_theta_offset(-np.pi / 2.0)  # Set 0 degrees at the bottom
#     ax.set_yticks([])  # Remove radial ticks

#     # Add bars for each slice
#     ax.bar(
#         radians, 
#         1,  # Radius of 1 for all bars
#         width=np.deg2rad(360 / len(cake)),  # Each bar covers an equal slice
#         color=colors,
#         edgecolor='black'  # Optional: Add edge color for better visibility
#     )

#     plt.title('Status-Based Circle Plot', va='bottom')
#     plt.show()
