function save_images()
[filtered_image, original_image] = Q2;

filtered_filename = 'Filtered_Brain_Image.png';
imwrite(filtered_image, filtered_filename);

% original_filename = 'Original_Brain_Image.png';
% imwrite(original_image, original_filename);

end
