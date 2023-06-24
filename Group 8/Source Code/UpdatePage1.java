import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class UpdatePage1 implements ActionListener {

    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JTextField txt = new JTextField();
    JTextField txt2 = new JTextField();
    JButton button = new JButton();
    JFrame frm;
    int n, num, pos;
    int a[];
    UpdatePage1(int ar[], int index, JFrame frame1){

        a = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            a[f] = ar[f];
        }
        frm = frame1;

        label.setText("Position: ");
        label.setVisible(true);
        label.setBounds(30, 20, 70, 30);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt.setVisible(true);
        txt.setBounds(110, 27, 180, 22);
        txt.setPreferredSize(new Dimension(200, 30));

        label2.setText("Number: ");
        label2.setVisible(true);
        label2.setBounds(30, 55, 70, 30);
        label2.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt2.setVisible(true);
        txt2.setBounds(110, 60, 180, 22);
        txt2.setPreferredSize(new Dimension(200, 30));

        button.setText("Submit");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(110, 88, 75, 22);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 13));
        button.addActionListener(this);

        frame.setTitle("Update");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        frame.setBounds(490, 320, 350, 180);
        Image icon = new ImageIcon(this.getClass().getResource("update.png")).getImage();
        frame.setIconImage(icon);
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
            pos = Integer.parseInt(txt.getText());
            num = Integer.parseInt(txt2.getText());
            a[pos - 1] = num;
            frm.dispose();
            HomePage home = new HomePage(a, n);
            frame.dispose();
        }
    }
}
