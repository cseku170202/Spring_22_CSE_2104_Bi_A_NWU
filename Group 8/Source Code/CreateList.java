import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class CreateList implements ActionListener{
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JButton button = new JButton();
    JButton button2 = new JButton();
    JTextField textField = new JTextField();

    CreateList(){

        label.setText("Operations: ");
        label.setVisible(true);
        label.setFont(new Font("Times New Roman", Font.BOLD, 20));
        label.setBounds(10, 10, 110, 30);

        button2.setText("< Back");
        button2.setFocusable(false);
        button2.setBounds(10, 45, 90, 30);
        button2.setVisible(true);
        button2.addActionListener(this);

        button.setText("Create");
        button.setFocusable(false);
        button.setBounds(400, 88, 100, 30);
        button.setVisible(true);
        button.addActionListener(this);

        frame.setVisible(true);
        frame.setTitle("Operations");
        frame.setLayout(null);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        frame.setBounds(200, 100, 900, 670);
        frame.setBackground(Color.green);
        frame.add(label);
        frame.add(button);
        frame.add(button2);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            LinkedListApp linked = new LinkedListApp();
            frame.dispose();
        }

        if(e.getSource() == button2){
            LaunchPage launchPage = new LaunchPage();
            frame.dispose();
        }
    }
}
