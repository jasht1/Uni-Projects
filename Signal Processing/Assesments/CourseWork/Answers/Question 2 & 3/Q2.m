function [filtered_image, original_image] = convolve_brain_image()

original_image = imread('Brain_BW512x512.png');

kernel = [
  -1 -1 -1 -1 -1;
  -1 -1 -1 -1 -1;
  -1 -1 24 -1 -1;
  -1 -1 -1 -1 -1;
  -1 -1 -1 -1 -1
  ];

filtered_image = conv2(double(original_image), kernel, 'same'); % stops it adding extra elements

filtered_image = uint8(mat2gray(filtered_image) * 255); % to match original_image

end
