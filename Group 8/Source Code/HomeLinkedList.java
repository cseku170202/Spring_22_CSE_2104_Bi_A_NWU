import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HomeLinkedList implements ActionListener {
    JFrame frame = new JFrame("Operations");
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JTextField inputField = new JTextField();
    JButton button = new JButton();
    JButton button2 = new JButton();
    JButton button3 = new JButton();
    JButton button4 = new JButton();
    JButton button5 = new JButton();
    JButton button6 = new JButton();
    JTextArea textArea = new JTextArea();
    JFrame frm;
    private LinkedList linkedList = new LinkedList();
    private Node head;
    int n;

    HomeLinkedList(int j, LinkedList linkedLists, Node heads){
        frm = frame;
        n = j;
        linkedList = linkedLists;
        this.head = heads;

        label.setText("LinkedList Operations:");
        label.setVisible(true);
        label.setFont(new Font("Times New Roman", Font.BOLD, 20));
        label.setBounds(10, 10, 200, 30);

        label2.setText(n + " Elements are: ");
        label2.setVisible(true);
        label2.setFont(new Font("Times New Roman", Font.ITALIC, 24));
        label2.setBounds(120, 85, 160, 18);

        button2.setText("< Back");
        button2.setFocusable(false);
        button2.setBounds(10, 45, 90, 30);
        button2.setVisible(true);
        button2.addActionListener(this);

        textArea.setVisible(true);
        textArea.setEditable(false);
        Font f = new Font("Arial", Font.PLAIN, 18);
        textArea.setBounds(170, 115, 560, 400);
        textArea.setFont(f);
        Node temp = head;
        int i = 0;
        while(temp != null) {
                textArea.append(temp.data + " -> ");
                temp = temp.next;
        }

        button6.setText("Search");
        button6.setVisible(true);
        button6.setFocusable(false);
        button6.setBounds(170, 530, 90, 30);
        button6.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        button6.addActionListener(this);

        button3.setText("Insert");
        button3.setVisible(true);
        button3.setFocusable(false);
        button3.setBounds(328, 530, 90, 30);
        button3.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        button3.addActionListener(this);

        button4.setText("Update");
        button4.setVisible(true);
        button4.setFocusable(false);
        button4.setBounds(483, 530, 90, 30);
        button4.setFont(new Font("Times New Roman", Font.PLAIN, 18 ));
        button4.addActionListener(this);

        button5.setText("Delete");
        button5.setVisible(true);
        button5.setFocusable(false);
        button5.setBounds(640, 530, 90, 30);
        button5.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        button5.addActionListener(this);

        frame.setBounds(200, 100, 900, 670);
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);
        frame.setVisible(true);
        frame.add(label);
        frame.add(label2);
        frame.add(button2);
        frame.add(button3);
        frame.add(button4);
        frame.add(button5);
        frame.add(button6);
        frame.add(textArea);
        frame.add(button);

    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if(e.getSource() == button2){
            frame.dispose();
            LinkedListApp linked = new LinkedListApp();
        }

        if(e.getSource() == button6){
            L_SearchOpt lSearchOpt = new L_SearchOpt(n, linkedList, linkedList.head);
        }

        if(e.getSource() == button3){
            L_InsertOpt lInsertOpt = new L_InsertOpt(n, linkedList, linkedList.head, frm);
        }

        if(e.getSource() == button4){
            L_UpdateOpt lUpdateOpt = new L_UpdateOpt(n, linkedList, linkedList.head, frm);
        }

        if(e.getSource() == button5){
            L_DeleteOpt lDeleteOpt = new L_DeleteOpt(n, linkedList, linkedList.head, frm);
        }
    }
}
