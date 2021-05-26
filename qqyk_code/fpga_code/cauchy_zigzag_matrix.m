% finite_field_size = 5;
% x_set_size = 10;
% y_set_size = 20;
% 
% x_set = [gf(0, 5)];
% for x_set_num = 0:x_set_size-1
%     x_set(1, x_set_num+1) = gf(x_set_num, finite_field_size);
% end
% % x_set
% 
% y_set = [gf(0, 5)];
% for y_set_num = 10:10+y_set_size-1
%     y_set(1, y_set_num-9) = gf(y_set_num, finite_field_size);
% end
% % y_set
% cauchy_matrix = [gf(0, 5)];
% 
% for row_index = 1:x_set_size
%    for column_index = 1:y_set_size
%       cauchy_matrix(row_index, column_index) = gf(1, finite_field_size)/(x_set(row_index) + y_set(column_index)) ;
%    end
% end
% cauchy_matrix;

cauchy_matrix = ...
[25          16           7          15           6          13          11          24           2          29          30          26           8           5     17          10          21          31           3          19;
 16          25          15           7          13           6          24          11          29           2          26          30           5           8     10          17          31          21          19           3;
 22           4           6          13           7          15           2          29          11          24           8           5          30          26     21          31          17          10          20          27;
  4          22          13           6          15           7          29           2          24          11           5           8          26          30     31          21          10          17          27          20;
  6          13          22           4          25          16          30          26           8           5          11          24           2          29      3          19          20          27          17          10;
 13           6           4          22          16          25          26          30           5           8          24          11          29           2     19           3          27          20          10          17;
  7          15          25          16          22           4           8           5          30          26           2          29          11          24     20          27           3          19          21          31;
 15           7          16          25           4          22           5           8          26          30          29           2          24          11     27          20          19           3          31          21;
 18          28           9          23          14          12          17          10          21          31           3          19          20          27     11          24           2          29          30          26;
 28          18          23           9          12          14          10          17          31          21          19           3          27          20     24          11          29           2          26          30];
element_shift_vector = [0   1   18  2   5   19  11  3   29  6 ...
                        27  20  8   12  23  4   10  30  17  7 ...
                        22  28  26  21  25  9   16  13  14  24 ...
                        15];
cauchy_shift_matrix = ones(10, 20);
for row_index = 1:x_set_size
   for column_index = 1:y_set_size
      cauchy_shift_matrix(row_index, column_index) = element_shift_vector(cauchy_matrix(row_index, column_index)) ;
   end
end
cauchy_shift_matrix
% find max element in each row
for row_index = 1:x_set_size
    max_element = max(cauchy_shift_matrix(row_index,:));
    fprintf('max_element:%d\n', max_element);
end

