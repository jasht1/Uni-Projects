% function Vary_Kernal_Size()

original_image = double(imread('Brain_BW512x512.png'));

kernels = [-24,0,24,25,50];
num_kernels = length(kernels);

figure('Name', 'Effect of Different Kernel Centre Values');

for i = 1:num_kernels
  kernel = ones(5,5)*-1;
  midpont = 3;
  centre_val = kernels(i);
  kernel(midpont,midpont) = centre_val;
  
  filtered_image = conv2(original_image, kernel, 'same'); % stops it adding extra elements
  
  filtered_image = uint8(mat2gray(filtered_image) * 255); % to match original_image
  
  % Plot the filtered image
  subplot(1, num_kernels, i);
  imshow(filtered_image);
  title(sprintf('Centre Value: %d', centre_val), 'FontSize', 10);
  axis image off;
end
% end
