# ROS
## 実行方法
1. 1つ目のターミナル  
`roscore`
1. 2つ目のターミナル  
`rosrun mypkg input.py`
1. ３つ目のターミナル  
`rosrun mypkg calc.py`  

## 動作
input.py側に整数で円の半径を入力するとcalc.py側で半径と円の面積、円周が出力され、OpenCVによってその円が表示される。
