   M S B A M L   `   `   `  ����B  >WpfApp2, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null!clr-namespace:WpfApp2WpfApp2  5   	       WpfApp2.MainWindow   5   	   \ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   'localclr-namespace:WpfApp2     5   	     � Title$  Task manager��5   	   $	��450��6   $	��450��6+   .��5	      �  � RowDefinitions 5
   
   �� 5      $��30 �6   �� 5      $��* �6   �� 5      $��35 �6   .+�5   
   � $��0��6   .+�5      �� -   5        $��	TimeLabel��5      $��Label��6(   $��Center=�68   $��Center=�6U   5      � 5   
   $��1��6   .+�5      �� -   5        $��ListViewMain��5      $��5q�6,    �� View 5      �� 5      P�5      �� 5      $
��Name��6-    �� DisplayMemberBinding 6;   ��  �� Path$
 Name�6h   �� 5      $	��CPU��6-    6:   �� $ CP�6e   �� 5      $��Memory��6-    6=   �� $	 RAM�6i   �� 5      $��
Time start��6-    6A   �� $ 	TimeStart�6s   �� 5      $��	Time left��6-    6@   �� $
 Time�6m   5       5"      5#      � 5%   
   $��2��6    � ColumnDefinitions 5&      �� 5'      $��* �6#   �� 5(      $��* �6#   �� 5)      $��* �6#   .+�5,      �� -   5        $��	ButtonAdd��5,      $
��FCFS��6(   $��1��68   $��5q�6I   5-      �� 5.      -   5        $��
ButtonAlg1��5.      $	��ADD��6)   $��0��68   $��5q�6I   5/      �� 50      -   5        $��
ButtonAlg2��50      $��1��6(   $��RR��6<   $��2��6J   $��5q�6Z   51      52      53      55      