clear all
clc

without_data = csvread("ResultViTlossacc.csv ");
without_train_loss = without_data(:,1);
without_valid_loss = without_data(:,2);
without_train_accuracy = without_data(:,3);
without_valid_accuracy = without_data(:,4);
% 
with_data = csvread("WResultViTlossacc.csv");
with_train_loss = with_data(:,1);
with_valid_loss = with_data(:,2);
with_train_accuracy = with_data(:,3);
with_valid_accuracy = with_data(:,4);
% 
figure()
x1=1:length(without_train_loss);
x2=1:length(with_train_loss);
subplot(2,2,1)
plot(x1,without_train_accuracy,x1,without_valid_accuracy,"LineWidth",1)
legend("Training","Valid",'Fontname','Times New Roman','Location','SouthEast')
xlabel('Epoch(-)','FontSize',12,'Fontname','Times New Roman','Color','k')
ylabel('Accuracy','FontSize',12,'Fontname','Times New Roman','Color','k')
subplot(2,2,2)
plot(x2,with_train_accuracy,x2,with_valid_accuracy,"LineWidth",1)
legend("Training","Valid",'Fontname','Times New Roman','Location','SouthEast')
xlabel('Epoch(-)','FontSize',12,'Fontname','Times New Roman','Color','k')
ylabel('Accuracy','FontSize',12,'Fontname','Times New Roman','Color','k')
subplot(2,2,3)
plot(x1,without_train_loss,x1,without_valid_loss,"LineWidth",1)
legend("Training","Valid",'Fontname','Times New Roman','Location','NorthEast')
xlabel({'Epoch(-)','(a)'},'FontSize',12,'Fontname','Times New Roman','Color','k')
ylabel('Loss','FontSize',12,'Fontname','Times New Roman','Color','k')
subplot(2,2,4)
plot(x2,with_train_loss,x2,with_valid_loss,"LineWidth",1)
legend("Training","Valid",'Fontname','Times New Roman','Location','NorthEast')
xlabel({'Epoch(-)','(b)'},'FontSize',12,'Fontname','Times New Roman','Color','k')
ylabel('Loss','FontSize',12,'Fontname','Times New Roman','Color','k')


