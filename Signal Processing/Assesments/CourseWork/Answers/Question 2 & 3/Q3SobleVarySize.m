function Scaled_Sobel_Filter()

original_image = double(imread('Brain_BW512x512.png'));

kernel_sizes = [3, 5, 15, 31];
num_kernels = length(kernel_sizes);

figure('Name', 'Sobel Filter Scale Compare');
tiledlayout(num_kernels, 5);

%% smallest case
Gx = [
  -1 1;
  -1 1
  ];

Gy = [
  -1 -1;
  1  1
  ];

applyNplot(Gx,Gy,original_image);

for i = 1:num_kernels
  kernel_size = kernel_sizes(i);
  
  sigma = kernel_size/6;
  [Gx, Gy] = scale_sobel_kernels(kernel_size, sigma)
  
  applyNplot(Gx,Gy,original_image);
end
end

function applyNplot(Gx,Gy,original_image)
  % title(sprintf('%dx%d Sobel', kernel_size, kernel_size));

  % Apply convolution
  filtered_x = conv2(original_image, Gx, 'same');
  filtered_y = conv2(original_image, Gy, 'same');
  
  % Compute gradient magnitude
  sobel_magnitude = sqrt(filtered_x.^2 + filtered_y.^2);
  sobel_magnitude = mat2gray(sobel_magnitude);
  
  % Plot x
  nexttile;
  imagesc(Gx);
  axis image off;
  colormap('gray');

  nexttile;
  imshow(uint8(filtered_x) * 255);

  % Plot y
  nexttile;
  imagesc(Gy);
  axis image off;
  colormap('gray');

  nexttile;
  imshow(uint8(filtered_y) * 255);

  % final
  nexttile;
  imshow(uint8(sobel_magnitude * 255));
end

function [Gx, Gy] = scale_sobel_kernels(size, sigma)

half_size = floor(size/2);
x = -half_size:half_size;

% 1D Gaussian and its derivative
gauss = exp(-(x.^2)/(2*sigma^2));
gauss = gauss / sum(gauss); % Normalize

dgauss = -(x/sigma^2).*gauss; % Derivative of Gaussian

% 2D Sobel kernels
Gx = dgauss' * gauss; % Derivative along x
Gy = gauss' * dgauss; % Derivative along y
end
