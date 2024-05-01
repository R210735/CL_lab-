% Writing to a file
fid = fopen('example.txt', 'w');
fprintf(fid, 'Hello, world!\n');
fprintf(fid, 'This is a sample text file.\n');
fclose(fid);

% Reading from a file
fid = fopen('example.txt', 'r');
while ~feof(fid)
    line = fgetl(fid);
    disp(line);
end
fclose(fid);
