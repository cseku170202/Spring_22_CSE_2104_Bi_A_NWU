import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LaunchPage implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JButton button = new JButton();
    JButton button2 = new JButton();
    JButton button3 = new JButton();
    LaunchPage(){

        label.setText("Operations: ");
        label.setVisible(true);
        label.setFont(new Font("Times New Roman", Font.BOLD, 20));
        label.setBounds(10, 10, 110, 30);

        button.setText("Array");
        button.setFocusable(false);
        button.setBounds(400, 90, 100, 30);
        button.setVisible(true);
        button.addActionListener(this);

        button2.setText("Linked List");
        button2.setFocusable(false);
        button2.setBounds(400, 130, 100, 30);
        button2.setVisible(true);
        button2.addActionListener(this);

        button3.setText("[<- Exit");
        button3.setFocusable(false);
        button3.setBounds(10, 45, 90, 30);
        button3.setVisible(true);
        button3.addActionListener(this);

        frame.setVisible(true);
        frame.setTitle("Operations");
        frame.setLayout(null);
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        frame.setBounds(200, 100, 900, 670);
        frame.setBackground(Color.green);
        frame.add(label);
        frame.add(button);
        frame.add(button2);
        frame.add(button3);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            CreatePage create = new CreatePage();
            frame.dispose();
        }
        if(e.getSource() == button2){
            CreateList create = new CreateList();
            frame.dispose();
        }
        if(e.getSource() == button3){
            frame.dispose();
        }
    }
}
