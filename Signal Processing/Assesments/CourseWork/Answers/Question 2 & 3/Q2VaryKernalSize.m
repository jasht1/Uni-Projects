% function Vary_Kernal_Size()

original_image = double(imread('Brain_BW512x512.png'));

kernels = 1:4:17;
num_kernels = length(kernels);

figure('Name', 'Effect of Different Kernel Sizes');
% tiledlayout(2, num_kernels);

for i = 1:num_kernels
  kernel_size = kernels(i);
  kernel = ones(kernel_size,kernel_size)*-1;
  midpont = ceil(kernel_size/2);
  % if kernel_size == 1
  %   centre_val = 1; % otherwise it gets set to 0
  % else
  %   centre_val = kernel_size^2 - 1;
  % end
  centre_val = sum(kernel,"all") * -1;
  kernel(midpont,midpont) = centre_val;
  
  filtered_image = conv2(original_image, kernel, 'same'); % stops it adding extra elements
  
  filtered_image = uint8(mat2gray(filtered_image) * 255); % to match original_image
  
  % Plot the kernel
  % nexttile(i);
  subplot(2, num_kernels, i);
  imagesc(kernel);
  axis image off;
  colormap('gray');
  title(sprintf('%dx%d Kernel', kernel_size, kernel_size), 'FontSize', 10);
  
  % Plot the filtered image
  % nexttile(i + num_kernels);
  subplot(2, num_kernels, i + num_kernels);
  imshow(filtered_image);
  axis image off;
end
% end
