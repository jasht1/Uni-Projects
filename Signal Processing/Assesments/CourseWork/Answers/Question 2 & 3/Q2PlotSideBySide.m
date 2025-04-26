
function save_convolution_images()
[filtered_image, original_image] = Q2;

original_filename = 'Original_Brain_Image.png';
filtered_filename = 'Filtered_Brain_Image.png';

imwrite(original_image, original_filename);
imwrite(filtered_image, filtered_filename);

end

function showAideBySide()
[filtered_image, original_image] = Q2;

% Create a figure and plot both images
figure('Name', 'Convolution Effect on Brain Image', 'NumberTitle', 'off');

subplot(1,2,1);
imshow(original_image);
title('Original Image');

subplot(1,2,2);
imshow(filtered_image);
title('Filtered Image');
end
