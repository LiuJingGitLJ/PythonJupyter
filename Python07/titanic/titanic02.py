import pandas

titanic = pandas.read_csv("input/train.csv")
print(titanic)
#通过describe（）方法发现Age特征中的数据有缺失，但是当前特征比较重要
#遂对Age特征进行数据填充(填充通过该特征的均值进行填充)
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
print(titanic.describe())
# 由于机器学习算法 转换为矩阵需要数值，而不能识别字符，则需要对部分特征 字符进行
# 转换，转换为数值，然后进行numpy 矩阵计算
#对数据进行去重,获取特征值，Sex的特征下的类别
print(titanic["Sex"].unique())

#替换性别的两个类别，用0代表male,1代表female
#字符到数值的转换
titanic.loc[titanic["Sex"] == "male", "Sex"] = 0
titanic.loc[titanic["Sex"] == "female", "Sex"] = 1

#输出Emarked特征下的类别
#输出后发现Embarked 下面有空值，但是由于是字符类型，使用均值不太合适，
#此时字符的缺失值，一般用最多的类别去填充，S最多，则填充S
print(titanic["Embarked"].unique())

titanic["Embarked"] = titanic["Embarked"].fillna('S')
print(titanic["Embarked"].unique())
#数值映射
titanic.loc[titanic["Embarked"] == "S", "Embarked"] = 0
titanic.loc[titanic["Embarked"] == "C", "Embarked"] = 1
titanic.loc[titanic["Embarked"] == "Q", "Embarked"] = 2

print(titanic.describe())