
field_size = 4;
set_x = [gf(0,field_size) gf(1,field_size) gf(2,field_size) gf(3,field_size)];
set_y = [gf(4,field_size) gf(5,field_size) gf(6,field_size) gf(7,field_size) gf(8,field_size) gf(9,field_size) gf(10,field_size) gf(11,field_size) gf(12,field_size) gf(13,field_size) gf(14,field_size) gf(15,field_size)];
% array = [gf(0,field_size) gf(1,field_size)];
encoding_matrix = [gf(0,field_size) gf(1,field_size) gf(2,field_size) gf(3,field_size)];

for index = 1:12
    encoding_matrix(index,:) = [gf(1,field_size)/(set_y(index) + set_x(1)) gf(1,field_size)/(set_y(index) + set_x(2)) gf(1,field_size)/(set_y(index) + set_x(3)) gf(1,field_size)/(set_y(index) + set_x(4))];

end

% for index = 1:7
%     num = gf(index, field_size);
%     gf(4,field_size) / num
% end