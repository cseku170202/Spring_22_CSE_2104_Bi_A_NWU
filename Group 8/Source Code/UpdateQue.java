import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UpdateQue implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JButton button = new JButton();
    JButton button1 = new JButton();
    int n, num, pos;
    int a[];
    JFrame frm;
    UpdateQue(int ar[], int index, JFrame frame1){

        a = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            a[f] = ar[f];
        }
        frm = frame1;

        label.setText("Update by: ");
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

        frame.setTitle("Update");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("update.png")).getImage();
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
            frame.dispose();
            UpdatePage1 update = new UpdatePage1(a, n, frm);
        }
        if(e.getSource() == button1){
            frame.dispose();
            UpdatePage2 update = new UpdatePage2(a, n, frm);
        }
    }
}
