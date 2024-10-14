file_read = xlsread('test_8.xlsx');


% XGE ECE94
Ax = file_read(2:end,1)';
Ay = file_read(2:end,2)';
Ares = file_read(2:end,3)';
time = file_read(2:end,4)';


figure;
%plot(time,A_max,'r');
hold on;
%plot(time,A_min,'r');
xlabel('time, ms');
ylabel('A, g');

plot(time,Ares,'b');

hold off;
title('Ares');

figure;
subplot(2,1,1);

%plot(time,coef_Ax*Axy_max,'r');
hold on;
%plot(time,coef_Ax*Axy_min,'r');

plot(time,Ax,'b');
title('Ax');
xlabel('time, ms');
ylabel('A, g');

subplot(2,1,2);

%plot(time,coef_Ay*Axy_max,'r');
hold on;
%plot(time,coef_Ay*Axy_min,'r');

plot(time,Ay,'b');
title('Ay');
xlabel('time, ms');
ylabel('A, g');