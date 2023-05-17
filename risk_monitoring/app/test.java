package app;
import quickfix.field.*;
import quickfix.*;
// import java.lang.*;
import org.quickfixj.*;


public class test {

    public static void main(String[] args){
        Message newOrderSingle = new Message();

        newOrderSingle.getHeader().setString(MsgType.FIELD, MsgType.ORDER_SINGLE);
        newOrderSingle.getHeader().setString(BeginString.FIELD, FixVersions.BEGINSTRING_FIX42);
        newOrderSingle.getHeader().setString(SenderCompID.FIELD, "SENDER");
        newOrderSingle.getHeader().setString(TargetCompID.FIELD, "RECEIVER");
        newOrderSingle.getHeader().setString(SendingTime.FIELD, "19980930-06:25:58");

        
        newOrderSingle.setString(ClOrdID.FIELD, "1234");
        newOrderSingle.setString(Symbol.FIELD, "AAPL");
        newOrderSingle.setChar(Side.FIELD, Side.BUY);
        newOrderSingle.setDouble(OrderQty.FIELD, 100);
        newOrderSingle.setDouble(Price.FIELD, 150.00);

        String fixString = newOrderSingle.toString();
        String fixString2 = "8=FIXT.1.19=34835=X34=5049=SERVER52=20230516-09:10:25.32356=CLIENT262=c417827e-edcd-4313-9773-e4c0c16f5cad1021=1268=2279=1269=0278=fa1612b3-3d7c-414f-8a1f-150610545f3155=CUSIP122=1270=147.83084595499895423=1271=915770.5885246183279=1269=1278=73eb1d23-428b-4af4-9ea3-ce6726e249c455=CUSIP122=1270=144.15414148105341423=1271=771145.689044536110=096";
            
        fixString = fixString.replace('\u0001', '|');
        fixString2 = fixString2.replace('\u0001', '|');

        try{
            System.out.println(fixString);
            System.out.println(fixString2);
        }
        // 8=FIX.4.2|9=40|35=D|49=SENDER|56=RECEIVER|11=1234|38=100|44=150|54=1|55=AAPL|10=098|
        // 8=FIX.4.2|9=70|35=D|49=SENDER|56=RECEIVER|34=1|52=20230516-10:00:00|11=ORDER_ID|55=AAPL|54=1|38=100|40=1|59=0|10=010|

        catch(Exception e){
            System.out.println(e.getMessage());
        }

    }


}
