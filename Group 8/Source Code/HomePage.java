import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class HomePage implements ActionListener {
    JFrame frame = new JFrame();
    JLabel label = new JLabel();
    JLabel label2 = new JLabel();
    JTextArea textArea = new JTextArea();
    JLabel label4 = new JLabel();
    JButton button = new JButton();
    JButton button2 = new JButton();
    JButton button3 = new JButton();
    JButton button4 = new JButton();
    JButton button5 = new JButton();
    int n;
    int a[];
    int i = 1, j = 0, k = 0;
    HomePage(int ar[], int index){

        a = new int[index];
        n = index;
        for(int f = 0; f < n; f ++){
            a[f] = ar[f];
        }

        label.setText("Array operations: ");
        label.setVisible(true);
        label.setFont(new Font("Times new Roman", Font.BOLD,20));
        label.setBounds(10, 10, 180, 30);

        button.setText("< Back");
        button.setFocusable(false);
        button.setBounds(10, 45, 90, 30);
        button.setVisible(true);
        button.addActionListener(this);

        label2.setText(index + " Elements are: ");
        label2.setVisible(true);
        label2.setFont(new Font("Times New Roman", Font.ITALIC, 24));
        label2.setBounds(120, 85, 160, 18);

        textArea.setVisible(true);
        Font f = new Font("Arial", Font.PLAIN, 18);
        textArea.setBounds(170, 115, 560, 400);
        textArea.setFont(f);
        textArea.setEditable(false);
        for(int j = 0; j < index; j ++){
            textArea.append(ar[j] + "    ");
            if(j != 0 && j % 9 == 0){
                textArea.append("\n");
            }
        }

        button2.setText("Search");
        button2.setVisible(true);
        button2.setFocusable(false);
        button2.setBounds(170, 530, 90, 30);
        button2.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        button2.addActionListener(this);

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
        button4.setFont(new Font("Times New Roman", Font.PLAIN, 18));
        button4.addActionListener(this);

        button5.setText("Delete");
        button5.setVisible(true);
        button5.setFocusable(false);
        button5.setBounds(640, 530, 90, 30);
        button5.setFont(new Font("Times New Roman", Font.PLAIN, 20));
        button5.addActionListener(this);

        frame.setTitle("Home - Array");
        frame.setLayout(null);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(200, 100, 900, 670);
        frame.getContentPane().setBackground(new Color(188, 194, 190));
        Image icon = new ImageIcon(this.getClass().getResource("arr.png")).getImage();
        frame.setIconImage(icon);
        frame.add(label);
        frame.add(label2);
        frame.add(textArea);
        frame.add(label4);
        frame.add(button);
        frame.add(button2);
        frame.add(button3);
        frame.add(button4);
        frame.add(button5);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource() == button){
            Numbers page = new Numbers(n);
            frame.dispose();
        }
        if(e.getSource() == button2){
            SearchQue que = new SearchQue(a, n, frame);
        }
        if(e.getSource() == button3){
            InsertQue que = new InsertQue(a, n, frame);
        }
        if(e.getSource() == button4){
            UpdateQue que = new UpdateQue(a, n, frame);
        }
        if(e.getSource() == button5){
            DeleteQue que = new DeleteQue(a, n, frame);
        }
    }
}
