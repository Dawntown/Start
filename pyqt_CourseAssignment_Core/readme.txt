这里一共有两个代码：Config.py  gxq_net.py
Config.py里面有些参数，详见Config.py的注释
gxq_net.py里面有四个函数：
    save_data，读取所有图片，转成灰度图保存成矩阵，并能返回矩阵
    train_model，训练模型的代码，保存模型
    model_batch_test，大量测试测试集，得到模型测试的准确率，返回准确率
    model_predict_image，测试一张图片，根据图片的路径+名称，返回预测的结果，并把预测的结果和参考的标签同时打印出来
