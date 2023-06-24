import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class L_InsertPage1 implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JTextField txt = new JTextField();
    JTextField txt2 = new JTextField();
    JButton button = new JButton();
    JFrame frm;
    public LinkedList linkedList = new LinkedList();
    private Node head;
    int n;
    L_InsertPage1(int i, LinkedList linkedLists, Node heads, JFrame frame1){
        frm = frame1;
        n = i;
        linkedList = linkedLists;
        this.head = heads;

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

        frame.setTitle("Insert");
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.DISPOSE_ON_CLOSE);
        Image icon = new ImageIcon(this.getClass().getResource("insert.png")).getImage();
        frame.setIconImage(icon);
        frame.setBounds(490, 320, 350, 180);
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
            int pos = Integer.parseInt(txt.getText());
            int num = Integer.parseInt(txt2.getText());
            int j = 1;
            Node temp = head;
            Node tmp = new Node(num);
            Node top = new Node(num);
            if(pos > n+1){
                frame.dispose();
                JOptionPane.showOptionDialog(null, "Not found Position: "+pos, "Information", JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, 0);
            }
            else if(pos == 1){
                top.next = head;
                head = top;
                frm.dispose();
                HomeLinkedList homelinked = new HomeLinkedList(n+1, linkedList, linkedList.head);
                frame.dispose();
            }
            else {
                while(temp != null){
                    if(j == pos-1) {
                        //tmp.data = num;
                        tmp.next = temp.next;
                        temp.next = tmp;
                    }
                    temp = temp.next;
                    j = j + 1;
                }
                frm.dispose();
                HomeLinkedList homelinked = new HomeLinkedList(n+1, linkedList, linkedList.head);
                frame.dispose();
            }
            System.out.println();
            Node tem = head;
            while(tem != null){
                System.out.print(tem.data+"->");
                tem = tem.next;
            }

        }
    }
}
