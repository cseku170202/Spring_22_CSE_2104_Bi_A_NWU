import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class L_InsertPage2 implements ActionListener {
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
    L_InsertPage2(int i, LinkedList linkedLists, Node heads, JFrame frame1){
        frm = frame1;
        n = i;
        linkedList = linkedLists;
        this.head = heads;

        label.setText("Num: ");
        label.setVisible(true);
        label.setBounds(30, 23, 70, 30);
        label.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt.setVisible(true);
        txt.setBounds(110, 27, 180, 23);
        txt.setPreferredSize(new Dimension(200, 30));

        label2.setText("Number: ");
        label2.setVisible(true);
        label2.setBounds(30, 55, 70, 30);
        label2.setFont(new Font("Times New Roman", Font.PLAIN, 18));

        txt2.setVisible(true);
        txt2.setBounds(110, 60, 180, 23);
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
            int num = Integer.parseInt(txt.getText());
            int number = Integer.parseInt(txt2.getText());
            int j = 0, count = 0;
            Node temp = head;
            while(temp != null){
                j = j + 1;
                if(temp.data == num){
                    count = 1;
                    break;
                }
                temp = temp.next;
            }
            if(count == 0){
                JOptionPane.showOptionDialog(null, "Not found Number: "+num, "Information", JOptionPane.CLOSED_OPTION, JOptionPane.INFORMATION_MESSAGE, null, null, 0);
            }
            else {
                Node top = new Node(number);
                Node tmp = new Node(number);
                int pos = j;
                System.out.println(pos);
                if(pos == 1){
                    top.next = head;
                    head = top;
                }
                else {
                    Node temp1 = head;
                    int k = 1;
                    while(temp1 != null){
                        if(k == pos-1) {
                            tmp.data = number;
                            tmp.next = temp1.next;
                            temp1.next = tmp;
                        }
                        temp1 = temp1.next;
                        k = k + 1;
                    }
                }
                frm.dispose();
                HomeLinkedList homelinked = new HomeLinkedList(n+1, linkedList, linkedList.head);
                frame.dispose();
            }
            Node tem = head;
            while(tem != null){
                System.out.print(tem.data+"->");
                tem = tem.next;
            }
        }
    }
}
