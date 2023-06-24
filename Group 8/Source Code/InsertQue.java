import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InsertQue implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JButton button = new JButton();
    JButton button1 = new JButton();
    int n, num, pos;
    int a[];
    JFrame frm;
    InsertQue(int ar[], int index, JFrame frame1){

        a = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            a[f] = ar[f];
        }

        frm = frame1;
        label.setText("Insert by: ");
        label.setVisible(true);
        label.setBounds(15, 5, 100, 30);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        button.setText("Position");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(90, 40, 150, 28);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 15));
        button.addActionListener(this);

        button1.setText("Number");
        button1.setVisible(true);
        button1.setFocusable(false);
        button1.setBounds(90, 75, 150, 28);
        button1.setFont(new Font("Times New Roman", Font.PLAIN, 15));
        button1.addActionListener(this);

        frame.setTitle("Insert");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("insert.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label);
        frame.add(button);
        frame.add(button1);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            InsertPage1 insert = new InsertPage1(a, n, frm);
            frame.dispose();
        }
        if(e.getSource() == button1){
            InsertPage2 insert = new InsertPage2(a, n, frm);
            frame.dispose();
        }
    }
}
