import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class L_InsertOpt implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label1 = new JLabel();
    JTextField text = new JTextField();
    JButton button = new JButton();
    JButton button1 = new JButton();
    JFrame frm;
    public LinkedList linkedList = new LinkedList();
    private Node head;
    int n;
    L_InsertOpt(int i, LinkedList linkedLists, Node heads, JFrame frame1){
        frm = frame1;
        n = i;
        linkedList = linkedLists;
        this.head = heads;

        label1.setText("Insert by: ");
        label1.setVisible(true);
        label1.setBounds(15, 5, 100, 30);
        label1.setFont(new Font("Times New Roman", Font.PLAIN, 18));

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

        frame.setTitle("Search");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("insert.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
        frame.setLayout(null);
        frame.add(label1);
        frame.add(button);
        frame.add(button1);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            frame.dispose();
            L_InsertPage1 linsertpage1 = new L_InsertPage1(n, linkedList, linkedList.head, frm);
        }

        if(e.getSource() == button1){
            frame.dispose();
            L_InsertPage2 linsertpage2 = new L_InsertPage2(n, linkedList, linkedList.head, frm);
        }
    }
}
