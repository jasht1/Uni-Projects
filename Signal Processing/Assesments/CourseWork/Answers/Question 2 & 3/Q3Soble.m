function Brain_Sobel_Filter()
original_image = double(imread('Brain_BW512x512.png'));
% original_image = double(imread('Filtered_Brain_Image.png'));

% Sobel kernels

Gx = [
  -1 0 1;
  -2 0 2;
  -1 0 1
  ];

Gy = [
  -1 -2 -1;
  0  0  0;
  1  2  1
  ];

% Apply convolution
filtered_x = conv2(original_image, Gx);
filtered_y = conv2(original_image, Gy);

% Compute gradient magnitude
sobel_magnitude = sqrt(filtered_x.^2 + filtered_y.^2);

sobel_magnitude = mat2gray(sobel_magnitude);

% Plot results
figure('Name', 'Sobel Filter Results');
tiledlayout(1,4);

nexttile;
imshow(uint8(original_image));
title('Original Image');

nexttile;
imshow(uint8(mat2gray(filtered_x)) * 255);
title('Sobel Horizontal');

nexttile;
imshow(uint8(mat2gray(filtered_y)) * 255);
title('Sobel Vertical');
nexttile;

imshow(uint8(sobel_magnitude * 255));
title('Gradient Magnitude');
end
