// Generated by gencpp from file dreambot/ReachGoalGoal.msg
// DO NOT EDIT!


#ifndef DREAMBOT_MESSAGE_REACHGOALGOAL_H
#define DREAMBOT_MESSAGE_REACHGOALGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace dreambot
{
template <class ContainerAllocator>
struct ReachGoalGoal_
{
  typedef ReachGoalGoal_<ContainerAllocator> Type;

  ReachGoalGoal_()
    : start(false)  {
    }
  ReachGoalGoal_(const ContainerAllocator& _alloc)
    : start(false)  {
  (void)_alloc;
    }



   typedef uint8_t _start_type;
  _start_type start;





  typedef boost::shared_ptr< ::dreambot::ReachGoalGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::dreambot::ReachGoalGoal_<ContainerAllocator> const> ConstPtr;

}; // struct ReachGoalGoal_

typedef ::dreambot::ReachGoalGoal_<std::allocator<void> > ReachGoalGoal;

typedef boost::shared_ptr< ::dreambot::ReachGoalGoal > ReachGoalGoalPtr;
typedef boost::shared_ptr< ::dreambot::ReachGoalGoal const> ReachGoalGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::dreambot::ReachGoalGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::dreambot::ReachGoalGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::dreambot::ReachGoalGoal_<ContainerAllocator1> & lhs, const ::dreambot::ReachGoalGoal_<ContainerAllocator2> & rhs)
{
  return lhs.start == rhs.start;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::dreambot::ReachGoalGoal_<ContainerAllocator1> & lhs, const ::dreambot::ReachGoalGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace dreambot

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::dreambot::ReachGoalGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::dreambot::ReachGoalGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::dreambot::ReachGoalGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "676aa7bfb3ec2071e814f2368dfd5fb5";
  }

  static const char* value(const ::dreambot::ReachGoalGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x676aa7bfb3ec2071ULL;
  static const uint64_t static_value2 = 0xe814f2368dfd5fb5ULL;
};

template<class ContainerAllocator>
struct DataType< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "dreambot/ReachGoalGoal";
  }

  static const char* value(const ::dreambot::ReachGoalGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"# Control.action\n"
"bool start  # Goal - whether to start or stop the controller\n"
;
  }

  static const char* value(const ::dreambot::ReachGoalGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.start);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ReachGoalGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::dreambot::ReachGoalGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::dreambot::ReachGoalGoal_<ContainerAllocator>& v)
  {
    s << indent << "start: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.start);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DREAMBOT_MESSAGE_REACHGOALGOAL_H
