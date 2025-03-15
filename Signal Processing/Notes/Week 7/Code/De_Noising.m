
pic1 = "Images/Road.jpg";
pic2 = "Images/Sam_Eth.jpg";

image = imread(pic1);

[r, g, b] = imsplit(image);
rgb = {r,g,b};

for channel = 1:3
  image = rgb{channel};
  rgb(channel) = medfilt2(image);
end

image = cat(3, r,g,b);
figure;
imshow(image);
impixelinfo()
