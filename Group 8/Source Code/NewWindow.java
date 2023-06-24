import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class NewWindow implements ActionListener{
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JLabel label3 = new JLabel();
    JButton button = new JButton();
    JButton button2 = new JButton();
    JTextField textField = new JTextField();
    int n;
    NewWindow(){

        label.setText("Operation > Array: ");
        label.setVisible(true);
        label.setBounds(10, 10, 180, 30);
        label.setFont(new Font("Times New Roman", Font.BOLD, 20));

        button2.setText("< Back");
        button2.setFocusable(false);
        button2.setBounds(10, 45, 90, 30);
        button2.setVisible(true);
        button2.addActionListener(this);

        label2.setText("Size of the Array: ");
        label2.setVisible(true);
        label2.setBounds(200, 90, 140, 20);
        label2.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        textField.setPreferredSize(new Dimension(200, 20));
        textField.setBounds(350, 89, 200, 25);
        textField.setVisible(true);

        button.setText("Next");
        button.setVisible(true);
        button.setBounds(350, 118, 75, 23);
        button.setFocusable(false);
        button.addActionListener(this);


        frame.setTitle("Operations");
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setBackground(Color.green);
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        frame.setBounds(200, 100, 900, 670);
        frame.add(label);
        frame.add(label2);
        frame.add(label3);
        frame.add(textField);
        frame.add(button);
        frame.add(button2);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            n = Integer.parseInt(textField.getText());
            Numbers page = new Numbers(n);
            frame.dispose();
            //System.out.println("Welcome "+ (n+1));
        }
        if(e.getSource() == button2){
            CreatePage create = new CreatePage();
            frame.dispose();
        }
    }

}
