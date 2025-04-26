function Vary_Kernal_Surroundings()

original_image = double(imread('Brain_BW512x512.png'));

kernel_surrounding = [10,1,-1,-10,-100];
num_kernels = length(kernels);

figure('Name', 'Effect of Different Kernel Sizes');

for i = 1:num_kernels
  kernel = ones(5,5)*kernel_surrounding(i);
  midpont = 3;
  centre_val = sum(kernel,"all") * -1;
  kernel(midpont,midpont) = centre_val;
  
  filtered_image = conv2(original_image, kernel, 'same'); % stops it adding extra elements
  
  filtered_image = uint8(mat2gray(filtered_image) * 255); % to match original_image
  
  % Plot the filtered image
  subplot(1, num_kernels, i);
  imshow(filtered_image);
  title(sprintf('Surrounding Value: %d', kernel_surrounding(i)), 'FontSize', 10);
end
end
