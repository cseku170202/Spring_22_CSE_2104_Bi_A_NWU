import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InsertPage2 implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JTextField txt = new JTextField();
    JTextField txt2 = new JTextField();
    JButton button = new JButton();
    int n, num1, num2, pos;
    int arr[];
    int a[];
    JFrame frm;
    InsertPage2(int ar[], int index, JFrame frame1){

        arr = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            arr[f] = ar[f];
        }
        frm = frame1;

        label.setText("Num: ");
        label.setVisible(true);
        label.setBounds(30, 23, 70, 30);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt.setVisible(true);
        txt.setBounds(110, 27, 180, 23);
        txt.setPreferredSize(new Dimension(200, 30));

        label2.setText("Number: ");
        label2.setVisible(true);
        label2.setBounds(30, 55, 70, 30);
        label2.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt2.setVisible(true);
        txt2.setBounds(110, 60, 180, 23);
        txt2.setPreferredSize(new Dimension(200, 30));

        button.setText("Submit");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(110, 88, 75, 22);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 13));
        button.addActionListener(this);

        frame.setTitle("Insert");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("insert.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label);
        frame.add(label2);
        frame.add(txt);
        frame.add(txt2);
        frame.add(button);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            num1 = Integer.parseInt(txt.getText());
            num2 = Integer.parseInt(txt2.getText());
            for (int f = 0; f < n; f++) {
                if(arr[f] == num1){
                    pos = f+1;
                    break;
                }
            }
            if(pos == 0) {
                frame.dispose();
                JOptionPane.showOptionDialog(null, "Not Found "+num1, "Warning!", JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, 0);
            }
            else {
                a = new int[n+1];
                for(int i = 0; i < n + 1; i ++){
                    if(i < pos - 1){
                        a[i] = arr[i];
                    }
                    else if (i == pos - 1){
                        a[i] = num2;
                    }
                    else {
                        a[i] = arr[i-1];
                    }
                }
                frm.dispose();
                HomePage home = new HomePage(a, n+1);
                frame.dispose();
            }
        }
    }
}
