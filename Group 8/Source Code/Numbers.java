import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Numbers implements ActionListener{
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JLabel label3 = new JLabel();
    JButton button = new JButton();
    JButton button2 = new JButton();
    JButton button3 = new JButton();
    JTextField txt = new JTextField();
    JTextArea ta = new JTextArea();
    int i = 0;
    int ar[];
    int num;
    int index;
    Numbers(int n){
        index = n;

        label.setText("Operations > Arrays > Elements: ");
        label.setFont(new Font("Times New Roman", Font.BOLD, 20));
        label.setBounds(10, 10, 300, 30);
        label.setVisible(true);

        button.setText("< Back");
        button.setFocusable(false);
        button.setBounds(10, 45, 90, 30);
        button.setVisible(true);
        button.addActionListener(this);

        label2.setText(n+" Elements are: ");
        label2.setVisible(true);
        label2.setFont(new Font("Times New Roman", Font.ITALIC, 18));
        label2.setBounds(110, 90, 150, 18);

        label3.setText("Element "+(i+1)+": ");
        label3.setVisible(true);
        label3.setFont(new Font("Times New Roman", Font.PLAIN, 16));
        label3.setBounds(250, 130, 90, 20);

        button2.setText("Submit");
        button2.setVisible(true);
        button2.setFocusable(false);
        button2.setBounds(491, 128, 75, 22);
        button2.addActionListener(this);

        button3.setText("Finish");
        button3.setVisible(true);
        button3.setFocusable(false);
        button3.setBounds(340, 153, 75, 20);
        button3.addActionListener(this);
        button3.setEnabled(false);

        txt.setVisible(true);
        txt.setPreferredSize(new Dimension(200, 21));
        txt.setBounds(340, 128, 150, 23);

        ta.setVisible(true);
        ta.setBounds(140, 450, 600, 100);
        Font f = new Font("Arial", Font.PLAIN, 12);
        ta.setFont(f);
        ta.setEditable(false);

        frame.setTitle("Operations");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        frame.setBounds(200, 100, 900, 670);
        frame.setLayout(null);
        frame.add(label);
        frame.add(label2);
        frame.add(label3);
        frame.add(button);
        frame.add(button2);
        frame.add(button3);
        frame.add(txt);
        frame.add(ta);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == button) {
            NewWindow page2 = new NewWindow();
            frame.dispose();
        }
        if (e.getSource() == button2) {
            if (i == 0) {
                ar = new int[index];

            }
            num = Integer.parseInt(txt.getText());
            ar[i] = num;
            label3.setText("Element "+(i+2)+": ");
            txt.setText("");
            ta.append(num+"  ");
            if(i == 19){
                ta.append("\n");
            }
            i++;
            if(i == index){
                label3.setText("Element "+(i)+": ");
                txt.setEnabled(false);
                button2.setEnabled(false);
                button3.setEnabled(true);
            }
        }
        if(e.getSource() == button3){
            HomePage home = new HomePage(ar, index);
            frame.dispose();

        }
    }
}
