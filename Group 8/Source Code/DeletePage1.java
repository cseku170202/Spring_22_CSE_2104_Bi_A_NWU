import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class DeletePage1 implements ActionListener {

    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JTextField txt = new JTextField();
    JButton button = new JButton();
    int num;
    int n;
    int a[];
    int pos = 0;
    JFrame frm;
    DeletePage1(int ar[], int index, JFrame frame1){

        a = new int[index];
        n = index;
        for(int f = 0; f < index; f ++){
            a[f] = ar[f];
        }
        frm = frame1;

        label.setText("Position: ");
        label.setVisible(true);
        label.setBounds(30, 25, 70, 30);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt.setVisible(true);
        txt.setBounds(110, 30, 180, 22);
        txt.setPreferredSize(new Dimension(200, 30));

        button.setText("Submit");
        button.setVisible(true);
        button.setFocusable(false);
        button.setBounds(110, 55, 75, 22);
        button.setFont(new Font("Times New Roman", Font.PLAIN, 13));
        button.addActionListener(this);

        frame.setTitle("Delete");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("delete.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label);
        frame.add(txt);
        frame.add(button);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            pos = Integer.parseInt(txt.getText());
            for(int j = pos; j < n; j ++){
                a[j - 1] = a[j];
            }
            frm.dispose();
            HomePage home = new HomePage(a, n-1);
            frame.dispose();
        }
    }
}
